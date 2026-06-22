from math import ceil

class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / cls.PHOTOS_PER_PAGE)
        return cls(pages)
    
    def add_photo(self, label):
        for page in range(self.pages):
            if len(self.photos[page]) < self.PHOTOS_PER_PAGE:
                self.photos[page].append(label)
                slot = len(self.photos[page])
                return f"{label} photo added successfully on page {page + 1} slot {slot}"
        return "No more free slots"
    
    def display(self):
        result = ["-----------"]
        for page in self.photos:
            result.append(" ".join("[]" for _ in range(len(page))))
            result.append("-----------")
        return "\n".join(result)