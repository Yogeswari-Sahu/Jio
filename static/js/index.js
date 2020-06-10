!(function($) {
    "use strict";
    
    // Toggle .header-scrolled class to #header when page is scrolled
    $(window).scroll(function() {
      if ($(this).scrollTop() > 100) {
        $('#header').addClass('header-scrolled');
      } else {
        $('#header').removeClass('header-scrolled');
      }
    });
  
    if ($(window).scrollTop() > 100) {
      $('#header').addClass('header-scrolled');
    }
  
    // Back to top button
    $(window).scroll(function() {
      if ($(this).scrollTop() > 100) {
        $('.back-to-top').fadeIn('slow');
      } else {
        $('.back-to-top').fadeOut('slow');
      }
    });
  
    $('.back-to-top').click(function() {
      $('html, body').animate({
        scrollTop: 0
      }, 1500, 'easeInOutExpo');
      return false;
    });
  
    // Porfolio isotope and filter
    $(window).on('load', function() {
      var portfolioIsotope = $('.portfolio-container').isotope({
        itemSelector: '.portfolio-item'
      });
  
      $('#portfolio-flters li').on('click', function() {
        $("#portfolio-flters li").removeClass('filter-active');
        $(this).addClass('filter-active');
  
        portfolioIsotope.isotope({
          filter: $(this).data('filter')
        });
        aos_init();
      });
    });
    
    // Initi AOS
    function aos_init() {
      AOS.init({
        duration: 1000,
        once: true
      });
    }
    $(window).on('load', function() {
      aos_init();
    });
  
  })(jQuery);


  // var formData = JSON.stringify($("#myForm").serializeArray());
  // $.ajax({
  //   type: "POST",
  //   url: "serverUrl",
  //   data: formData,
  //   success: function(){},
  //   dataType: "json",
  //   contentType : "application/json"
  // });


  /*
  for (x in brand_list) {
    document.getElementById("Brand").innerHTML +="<option value= \" " + x + " \">"+ x +"</option>";
  }

  $(function() {
    $('#document').ready(function() {
      //$('#debug_msg').text("Printed !!")
      let dropdown = $('#price_segment');
      dropdown.empty();
      dropdown.append('<option selected="true" disabled>Price Segments</option>');
      dropdown.prop('selectedIndex', 0);
      const url = '/loadpslist';
      $.getJSON(url, function (data) {
        $.each(data, function (key, entry) {
          dropdown.append($('<option></option>').attr('value', entry.abbreviation).text(entry.name));
        })
      });
    });
  });
/*
  $('#table').on('click', function(){

    $.ajax({
        type: "POST",
        url: "/get_table",
        contentType: 'application/json; charset=UTF-8',
        data: JSON.stringify({'row1': [1, 'honda', 'accord', 2004] ,
                              'row2': [2, 'toyota', 'camry', 2006]}),
        dataType: 'json',
        success: function(data){
            $('#product-table').html(data);
        },
        error: function(error){
            console.log(error);
        },

    });
});
/*
  function productUpdate() {
    if ($("#Product").value() != null &&
        $("#Product").value() != '') {
      // Add product to Table
      addRow();
      // Clear form fields
      formClear();
    }
  }
  function formClear() {
    $("#Product").value("");
    $("#Quantity").value("");
  }

  function addRow() {
          
    var prod = document.getElementById("Product");
    var quant = document.getElementById("Quantity");
    var table = document.getElementById("product-table");
 
    var rowCount = table.rows.length;
    var row = table.insertRow(rowCount);
 
    row.insertCell(0).innerHTML= prod.value;
    row.insertCell(1).innerHTML= quant.value;
 
}
  */

 /*$(function() {
  $("#submit").click(function() {

      var prod = $("input#productAdd").val();
      var quant = $("input#quantity").val();

      var dataString = [prod, quant];
      var n = dataString.length;

      $.ajax({
          type: "POST",
          url: "index.html",
          data: dataString,
          success: function() {
            var row = $('<tr>');
            for(var i = 0; i < n; i++) {
                row.append($('<td>').html(dataString[i]));
            }
            $('#results').append(row);
          }
      });
      return false;
  });
})*/




// window.addEventListener("DOMContentLoaded",event=>{
//     fetch("/sender")
//     .then(res=>{
//         return res.json()
//     })
//     .then(data=>{
        
                    
        // let html = ""
        // dataforEach(item=>{
        //     let prod = `<option value="${item}">${item}</option>`
        //     html+=prod
        // })

        // document.querySelector("#productAdd").innerHTML = html
        // document.querySelector("#products").innerHTML = html
//     })
// })
