import requests
import os
from abc import ABC, abstractmethod
from enum import Enum
from tqdm import tqdm
from .protocol import Protocol


def download_file(url: str, dst: str) -> None:
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    response = requests.get(url)
    with open(dst, "wb") as f:
        f.write(response.content)


class UnkownSite(Exception):
    pass


class downloaderSite(ABC):

    @abstractmethod
    def get_domain(self):
        raise NotImplementedError

    @abstractmethod
    def download(self, last_image_url: str):
        raise NotImplementedError


class DoujinSmart(downloaderSite):

    def get_domain(self):
        return "cdn.ddd-smart.net"

    def download(self, last_image_url: str, book_name: str):
        if os.path.exists(book_name):
            raise FileExistsError()

        folder = os.path.dirname(last_image_url)
        page_size = int(last_image_url.split("/")[-1].split(".")[0])
        to_folder = book_name
        offset = 0

        for i in tqdm(range(offset + 1, page_size + 1)):
            file = f"{str(i).zfill(3)}.jpg"
            # file = f"{str(i).zfill(3)}_{str(i).zfill(3)}"
            if not os.path.exists(f"data/{to_folder}/{i+offset}.jpg"):
                # sleep(0.5)
                url = f"{folder}/{file}"
                print(url)
                # input()
                download_file(url, f"data/{to_folder}/{i+offset}.jpg")


class SiteEnum(Enum):
    DOUJIN_SMART = DoujinSmart()

    @classmethod
    def download(cls, last_image_url: str, book_name: str):
        if not Protocol.is_supported_protocol(last_image_url):
            raise ValueError("Unsupported protocol")

        if os.path.exists(book_name):
            raise FileExistsError()

        done_flag = False
        for site in SiteEnum:
            last_image_url
            if site.value.get_domain() in last_image_url:
                site._download(last_image_url, book_name)
                done_flag = True

        if not done_flag:
            raise UnkownSite()

    def _download(self, last_image_url: str, book_name: str):
        self.value.download(last_image_url, book_name)


if __name__ == "__main__":
    last_image_url = "https://cdn.ddd-smart.net/20231002/001/022.jpg"
    book_name = "白ネギ屋/はいぼくマリィちゃん"
    SiteEnum.download(last_image_url, book_name=book_name)
