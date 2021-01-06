//filter by category
$(document).on("click", "#category", function (event) {
  event.preventDefault();
  const categoryId = $(this).attr("value");

  $(".category-item.activ").removeClass("activ");
  $(this).addClass("activ");

  $.ajax({
    type: "GET",
    url: productListUrl,
    data: {category_id: categoryId,},
    dataType: "json",
    success: function (response) {
        $("#card-columns").html(response["products"]);
     },
    error: function (rs, e) {
      console.log(rs);
    },
  });
});
