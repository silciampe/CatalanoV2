class Utils:

  def __init__(self):
      pass

  @staticmethod
  def sanitize_data(data):
      return data.strip().strip('"')

  @staticmethod
  def format_image_path(folder, image):
      image = Utils.sanitize_data(image)
      return f"imagenes/{folder}/{image}"