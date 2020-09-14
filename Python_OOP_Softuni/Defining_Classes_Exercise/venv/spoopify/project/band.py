class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has" \
                   f" {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        albums_list = [a for a in self.albums if a.name == album_name]
        if albums_list:
            album = albums_list[0]
            if album.published:
                return f"Album has been published. It cannot be removed."
        return f"Album {album.name} is not found."

        self.albums.remove(album)
        return f"Album {album.name} has been removed."

    def details(self):
        result = f"Band {self.name}\n"

        for album in self.albums:
            result += f"{album.details()}\n"

        return result

