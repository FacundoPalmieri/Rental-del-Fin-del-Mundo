(function ($) {

  "use strict";





  $(document).ready(function () {

    // product single page
    var thumb_slider = new Swiper(".product-thumbnail-slider", {
      autoplay: true,
      loop: true,
      spaceBetween: 8,
      slidesPerView: 4,
      freeMode: true,
      watchSlidesProgress: true,
    });

    var large_slider = new Swiper(".product-large-slider", {
      autoplay: true,
      loop: true,
      spaceBetween: 10,
      effect: 'fade',
      thumbs: {
        swiper: thumb_slider,
      },
    });


    //switch javascript

    const switchInput = document.getElementById('flexSwitchCheckChecked');
    const contentElements = document.querySelectorAll('.content');
    const monthlyLabel = document.getElementById('monthly-label');
    const yearlyLabel = document.getElementById('yearly-label');


    yearlyLabel.classList.add('label-color'); // Set initial accent color to yearly label


    switchInput.addEventListener('change', function () {
      if (this.checked) {
        yearlyLabel.classList.add('label-color'); // Add color to label
        monthlyLabel.classList.remove('label-color'); // Remove color from label
      } else {
        monthlyLabel.classList.add('label-color'); // Add color to label
        yearlyLabel.classList.remove('label-color'); // Remove color from label
      }
    });

    contentElements.forEach(function (element) {
      if (element.classList.contains('yearly')) {
        element.style.display = 'block';
      } else {
        element.style.display = 'none';
      }
    });     // Set the price initial state


    switchInput.addEventListener('change', function () {
      if (this.checked) {

        contentElements.forEach(function (element) {
          if (element.classList.contains('yearly')) {
            element.style.display = 'block';
          } else {
            element.style.display = 'none';
          }
        });
      } else {

        contentElements.forEach(function (element) {
          if (element.classList.contains('monthly')) {
            element.style.display = 'block';
          } else {
            element.style.display = 'none';
          }
        });
      }
    });    // Add event listener to the switch input





    // rental swiper
    var rentalSwiper = new Swiper(".rental-swiper", {
      speed: 600,
      slidesPerView: 3,
      spaceBetween: 30,
      freeMode: true,
      loop: true,
      navigation: {
        nextEl: ".rental-swiper-next",
        prevEl: ".rental-swiper-prev",
      },
      breakpoints: {
        0: {
          slidesPerView: 1,
          spaceBetween: 20,
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 30,
        },
        1400: {
          slidesPerView: 3,
          spaceBetween: 30,
        },
      }
    });


    //testimonial swiper
    var testimonialSwiper = new Swiper(".testimonial-swiper", {
      loop: true,
      pagination: {
        el: ".swiper-pagination",
      },
    });




    //date picker
    $("#datepicker1, #datepicker2").datepicker({
      autoclose: true,
      todayHighlight: true,
    }).datepicker('update', new Date());



    // Animate on Scroll
    AOS.init({
      duration: 1000,
      once: true,
    })




  });


})(jQuery);

document.querySelectorAll('.anchor-link').forEach(link => {
  link.addEventListener('click', function(e) {
    // Prevent default anchor click behavior
    e.preventDefault();

    const hash = this.getAttribute('href');
    const target = document.querySelector(hash);
    if (target) {
      // Calculate the position: target position - desired offset
      const yPos = target.getBoundingClientRect().top + window.pageYOffset - 35;

      // Scroll to the target position
      window.scrollTo({top: yPos, behavior: 'smooth'});
    }
  });
});