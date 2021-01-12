           function plus() {
               document.getElementById("quantity").setCustomValidity("")
               let quantity = parseInt(document.getElementById("quantity").value) + 1;
               if (quantity <= productCount) {
                   document.getElementById("quantity").value = quantity;
               }
               console.log(quantity);
               console.log(document.getElementById("quantity").value);
           }

           function minus() {
               document.getElementById("quantity").setCustomValidity("")
               let quantity = parseInt(document.getElementById("quantity").value) - 1;
               if (quantity > 0) {
                   document.getElementById("quantity").value = quantity;
               }
           }
