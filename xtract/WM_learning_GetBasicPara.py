import numpy as np


class BasicPara(object):
    def __init__(self):
        self.basics = [[2,2,2],[1,1,1],[1,3,1],[1,1,3],[3,1,1],[1,3,3],[3,1,3],[3,3,1],[3,3,3]]
        self._proc_tiles()

    def _proc_tiles(self):
        self.tiles = []
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    self.tiles.append([i,j,k])

    def _cal_dis(self):
        basic_np = np.array(self.basics)
        tiles_np = np.array(self.tiles)

        diff = np.sum(np.square(basic_np[:,np.newaxis,:] - tiles_np),axis=2)

        self.diff = diff

    def _get_transfer(self):
        pass

    def _cal_regions(self,basic,tiles):
        diff = [-1,0,1]
        regions = []
        for i in diff:
            for j in diff:
                for k in diff: 
                    tmp = [basic[0]+i,basic[1]+j,basic[2]+k]
                    if (tmp in tiles and not tmp in self.basics):
                        regions.append(str(tmp[0])+str(tmp[1])+str(tmp[2]))
                        tiles.remove(tmp)

        basic = str(basic[0]) + str(basic[1]) + str(basic[2])

        return regions,basic



    def _div_regions(self):
        tiles = self.tiles
        transfer_dict = {}
        for i in self.basics:
            region,basics = self._cal_regions(i,tiles)
            for reg in region:
                transfer_dict[reg] = basics
       
        for basic in self.basics:
            prefix = str(basic[0]) + str(basic[1]) + str(basic[2])
            transfer_dict[prefix] = prefix


        self.transfer_dict = transfer_dict

    def Update(self):
        self._div_regions()

    def Get_transfer_dict(self):
        return self.transfer_dict

if __name__ == '__main__':
    a = BasicPara()
    a.Update()

    transfer_dict = a.Get_transfer_dict()

    for key, value in sorted(transfer_dict.items(), key=lambda x: x[0]): 
        print("{} : {}".format(key, value))
    

