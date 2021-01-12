           function plus(id, count) {
               document.getElementById(id).setCustomValidity("")
               let quantity = parseInt(document.getElementById(id).value) + 1;
               if (quantity <= count) {
                   document.getElementById(id).value = quantity;
               }
               console.log(quantity)
           }
           function minus(id) {
               document.getElementById(id).setCustomValidity("")
               let quantity = parseInt(document.getElementById(id).value) - 1;
               if (quantity > 0) {
                   document.getElementById(id).value = quantity;
               }
           }
