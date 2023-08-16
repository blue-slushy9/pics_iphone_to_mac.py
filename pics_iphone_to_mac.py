import os
import imagecapture

def move_pictures(source_path, destination_path, file_names):
  """Moves the specified file names from the source path to the destination path.

  Args:
    source_path: The path to the source directory.
    destination_path: The path to the destination directory.
    file_names: A list of file names to move.
  """

  for file_name in file_names:
    source_file_path = os.path.join(source_path, file_name)
    destination_file_path = os.path.join(destination_path, file_name)
    imagecapture.import_image(source_file_path, destination_file_path)

if __name__ == "__main__":
  source_path = "/path/to/iphone/photos"
  destination_path = "/path/to/mac/photos"
  file_names = ["file1.jpg", "file2.jpg", "file3.jpg"]
  move_pictures(source_path, destination_path, file_names)
