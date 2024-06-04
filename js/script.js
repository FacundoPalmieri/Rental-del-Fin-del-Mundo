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
    monthlyLabel.classList.add('label-color'); 

    switchInput.addEventListener('change', function () {
      if (this.checked) {
        yearlyLabel.classList.add('label-color'); // Add color to label
      } else {
        monthlyLabel.classList.add('label-color'); // Add color to label
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


    switchInput.click()


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

