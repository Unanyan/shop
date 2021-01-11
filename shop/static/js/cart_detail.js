        <script>
            //get product onclick confirm button
            $(document).on("click", "#bt{{ product.id }}", function (event) {
              event.preventDefault();
              const id = {{ product.id }};

              $.ajax({
                type: "GET",
                url: "{% url 'cart:cart_add' product.id %}",
                data: {product_id: id,},
                dataType: "json",
                success: function (response) {
                    //$("#td{{ product.id }}").html(response["product"]);
                    cnt = response["product"]["count"];
                    console.log({{ product.count }});
                 },
                error: function (rs, e) {
                  console.log(rs);
                },
              });
            });
            </script>


    <script>
       /* let isValid = true;
        function clic() {
            let buttons = document.getElementsByClassName("confirm");
            console.log(buttons);
            for (let i = 0; i < buttons.length; i++) {
                setTimeout(console.log(i), 3000);
                buttons[i].click();
            }
            //location.replace("{% url 'cart:checkout' %}");
        }*/
    </script>
