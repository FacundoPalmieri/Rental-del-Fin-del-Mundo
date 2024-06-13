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


    // Inicialización del Datepicker
    $(document).ready(function() {
    
        // Obtener fecha actual
        let today = new Date();
        // Ajustar hora deseada (9:00 AM)
        today.setHours(9, 0, 0, 0);
        // Obtener offset del timezone local en minutos
        let offset = today.getTimezoneOffset();
        // Ajustar la hora de acuerdo al offset
        today.setMinutes(today.getMinutes() - offset);
        // Obtener el elemento Fecha de retiro
        var pickUpDate = document.getElementById('pick-up-date');
        // Asignar el valor al input Fecha de retiro
        pickUpDate.value = today.toISOString().slice(0, -8);
        // Bloquear fechas anteriores
        pickUpDate.min = today.toISOString().slice(0, -8);
        // Sumar un dia a la fecha actual
        let tomorrow = new Date(today);
        tomorrow.setDate(tomorrow.getDate() + 1);
        // Asignar el valor al input Fecha de entrega
        var returnDate = document.getElementById('return-date');
        // Asignar el valor al input Fecha de entrega
        returnDate.value = tomorrow.toISOString().slice(0, -8);
        // Bloquear fechas anteriores
        returnDate.min = tomorrow.toISOString().slice(0, -8);

        // Restringir horario de retiro
        pickUpDate.addEventListener('input', function() {
          var selectedTime = new Date(this.value);
          if (selectedTime.getHours() < 9) {
            alert("Los retiros comienzan a partir de las 9:00hs");
              this.value = today.toISOString().slice(0, -8); // Volver a poner fecha inicial
          }
        });

        // Restringir horario de entrega
        returnDate.addEventListener('input', function() {
          var selectedReturnTime = new Date(this.value);
          if (selectedReturnTime.getHours() < 9) {
            alert("La entrega puede realizarse a partir de las 9:00hs");
              this.value = tomorrow.toISOString().slice(0, -8); // Volver a poner fecha inicial
          }
        });
  });
  




    // Animate on Scroll
    AOS.init({
      duration: 1000,
      once: true,
    })




  });


})(jQuery);

