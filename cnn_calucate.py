import torch
import torch.nn as nn


class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1 =nn.Conv2d(3,16,3,padding=0,stride=1,dilation=1)
        self.conv2=nn.Conv2d(16,32,3,padding=0,stride=1,dilation=1)

    def forward(self,x):
        x=self.conv1(x)
        x=self.conv2(x)
        return x

    def num_flat_features(self,x):
        size =x.size()[1:]
        num_features =1
        for s in size:
            num_features *=s
        return num_features



if __name__ == '__main__':
    from torchstat import  stat
    input=torch.randn([1,3,32,32])
    model =Net()
    stat(model,(3,32,32))
