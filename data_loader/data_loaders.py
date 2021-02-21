from torchvision import datasets, transforms
from base import BaseDataLoader

class BCDataLoader(BaseDataLoader):

    def __init__(self, data_dir, batch_size, shuffle=True, validation_split=0.3, num_workers=1, training=None):
        trsfm = transforms.Compose([
            transforms.RandomResizedCrop(224),
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,))
        ])
        self.data_dir = data_dir
        self.dataset = datasets.ImageFolder(root=self.data_dir,
                                            transform=trsfm)
        super().__init__(self.dataset, batch_size, shuffle, validation_split, num_workers)
