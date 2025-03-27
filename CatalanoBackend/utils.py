class Utils:

  def __init__(self):
      pass

  @staticmethod
  def sanitize_data(data):
      return data.strip().strip('"').strip()

  @staticmethod
  def format_image_path(folder, image):
      path = ''
      image = Utils.sanitize_data(image)
      if image and image.lower() != ".jpg":
        image = Utils.sanitize_data(image)
        path = f"imagenes/{folder}/{image}"
      return path
