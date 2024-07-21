var booksSwiper = new Swiper(".books-slider", {
  loop: true,
  centeredSlides: true,
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  speed: 1000, // Adjust the speed for smooth sliding
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    768: {
      slidesPerView: 2,
    },
    1024: {
      slidesPerView: 3,
    },
  },
  on: {
    init: function () {
      // Add smooth transition effect on image hover
      var images = this.slides.find("img");
      images.on("mouseenter", function () {
        $(this).addClass("swiper-slide-hover");
      });
      images.on("mouseleave", function () {
        $(this).removeClass("swiper-slide-hover");
      });
    },
  },
});

var featuredSwiper = new Swiper(".featured-slider", {
  spaceBetween: 10,
  loop: true,
  centeredSlides: true,
  autoplay: {
    delay: 9500,
    disableOnInteraction: false,
  },
  speed: 1000, // Adjust the speed for smooth sliding
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    450: {
      slidesPerView: 2,
    },
    768: {
      slidesPerView: 3,
    },
    1024: {
      slidesPerView: 4,
    },
  },
  on: {
    init: function () {
      // Add smooth transition effect on image hover
      var images = this.slides.find("img");
      images.on("mouseenter", function () {
        $(this).addClass("swiper-slide-hover");
      });
      images.on("mouseleave", function () {
        $(this).removeClass("swiper-slide-hover");
      });
    },
  },
});
