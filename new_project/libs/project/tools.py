import PIL.Image
import os.path
import logging


def make_thumbnails(filename, sizes):
    '''
    Resize original image to multiple thunbnails

    Args:
     - filename: name of source file that we use to make trumbnails
     - sizes: list of sizes with maximal allowed side ['100x100', '200x200']
    '''
    def get_default_thumbnail_filename(filename, size):
        path, ext = os.path.splitext(filename)
        return '{0}.{1}.{2}'.format(path, size, ext)

    def make_thumbnail(filename, size):
        size = [int(x) for x in size.split('x')]
        logging.info('file ' + filename)

        image = PIL.Image.open(filename)
        if image.mode not in ('L', 'RGB'):
            image = image.convert('RGB')
        image = image.resize(size, PIL.Image.ANTIALIAS)

        # get the thumbnail data in memory.
        output_filename = get_default_thumbnail_filename(filename, "{0}x{1}".format(*size))
        image.save(output_filename, image.format)
        return output_filename

    for size in sizes:
        make_thumbnail(filename, size)


def register_user(email, password=None, username=None, **kwargs):
    '''
    Creates new user.

    Args:
      - email: (required) correct email address to send welcome message
      - password: if password not given, than we send message with link to reset password
      - username: if not given, than user email as username
    '''
    return 'new user instance'
