from thumbnail_maker import ThumbnailMakerService

IMG_URLS = \
    ["https://homepages.cae.wisc.edu/~ece533/images/airplane.png",
     "https://homepages.cae.wisc.edu/~ece533/images/arctichare.png",
     "https://homepages.cae.wisc.edu/~ece533/images/baboon.png",
     "https://homepages.cae.wisc.edu/~ece533/images/barbara.png",
     "https://homepages.cae.wisc.edu/~ece533/images/boat.png",
     "https://homepages.cae.wisc.edu/~ece533/images/cat.png",
     "https://homepages.cae.wisc.edu/~ece533/images/fruits.png",
     "https://homepages.cae.wisc.edu/~ece533/images/girl.png",
     "https://homepages.cae.wisc.edu/~ece533/images/goldhill.png",
     "https://homepages.cae.wisc.edu/~ece533/images/lena.png",
     "https://homepages.cae.wisc.edu/~ece533/images/monarch.png",
     "https://homepages.cae.wisc.edu/~ece533/images/mountain.png",
     "https://homepages.cae.wisc.edu/~ece533/images/peppers.png",
     "https://homepages.cae.wisc.edu/~ece533/images/pool.png",
     "https://homepages.cae.wisc.edu/~ece533/images/sails.png",
     "https://homepages.cae.wisc.edu/~ece533/images/serrano.png",
     "https://homepages.cae.wisc.edu/~ece533/images/tulips.png",
     "https://homepages.cae.wisc.edu/~ece533/images/watch.png",
     "https://homepages.cae.wisc.edu/~ece533/images/zelda.png"
    ]
    
def test_thumbnail_maker():
    tn_maker = ThumbnailMakerService()
    tn_maker.make_thumbnails(IMG_URLS)
