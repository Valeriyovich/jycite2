$('.input_1').click(function(){
    $(this).val('').change(); 
});
$(document).ready(function(){
    async function allCompany(url) {
        try {
            const response = await fetch(url);
            const data = await response.json();
            var countries1 = data[0];
            var countries2 = data[1];
            var contr = data;
            var qqq=[];
            var xxx 
            


            const countries = countries1.map((item,index)=>item=item+' | '+countries2[index]).sort();
            

            function autocomplete(inp, arr) {
    /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/
            var currentFocus;
    /*execute a function when someone writes in the text field:*/
            inp.addEventListener("input", function (e) {
            var a, b, i, val = this.value.trim();
    /*close any already open lists of autocompleted values*/
            closeAllLists();
            if (!val) { return false; }
            currentFocus = -1;
    /*create a DIV element that will contain the items (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items ");
    // a.setAttribute("style", "position:absolute");
    /*append the DIV element as a child of the autocomplete container:*/
        var button = document.createElement("button");
        button.innerHTML += '+';
        this.parentNode.appendChild(a);
        var count = 0;
    /*for each item in the array...*/
        for (i = 0; i < arr.length; i++) {
    /*check if the item starts with the same letters as the text field value:*/
        if (val.length == 1) {
            if (arr[i].substr(0,1).toUpperCase().includes(val.toUpperCase()) & (count < 14))
                {
                count++;
                b = document.createElement("DIV");
                b.setAttribute("class","d-flex")
                xxx = document.createElement("div");
                xxx.setAttribute("class", "tickerCompany ")
                xxx.innerHTML = arr[i]
                // xxx += "<input type='submit' class='btn btn-xs ml-3 border-0 bg-light' value='+' id='button__submit__portfolio'>";
                // b.innerHTML = arr[i]
                b.appendChild(xxx)
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                var ticker = arr[i].split(' | ')
                
                
                
                    b.addEventListener("click", function (e) {
                        inp.value = this.getElementsByTagName("input")[0].value;      
                        window.location.replace("?stock=" + inp.value);            
                        closeAllLists();
                        
                     
                })
             
                
              
                
            a.appendChild(b);
            
                }
            }
    if (val.length == 2) {
        if (arr[i].substr(0,2).toUpperCase().includes(val.toUpperCase()) & (count < 14))
            {
                count++;
                b = document.createElement("DIV");
                b.setAttribute("class","d-flex")
                xxx = document.createElement("div");
                xxx.setAttribute("class", "tickerCompany")
                xxx.innerHTML = arr[i]
                // xxx += "<input type='submit' class='btn btn-xs ml-3 border-0 bg-light' value='+' id='button__submit__portfolio'>";
                // b.innerHTML = arr[i]
                b.appendChild(xxx)
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                var ticker = arr[i].split(' | ')
                b.addEventListener("click", function (e) {
                    inp.value = this.getElementsByTagName("input")[0].value;
                    window.location.replace("?stock=" + inp.value);            
                closeAllLists();
                });

      a.appendChild(b);
        }
    }
    if (val.length == 3 ) {
        if (arr[i].substr(0,3).toUpperCase().includes(val.toUpperCase()) & (count < 14))
            {
                count++;
                b = document.createElement("DIV");
                b.setAttribute("class","d-flex")
                xxx = document.createElement("div");
                xxx.setAttribute("class", "tickerCompany")
                xxx.innerHTML = arr[i]
                // xxx += "<input type='submit' class='btn btn-xs ml-3 border-0 bg-light' value='+' id='button__submit__portfolio'>";
                // b.innerHTML = arr[i]
                b.appendChild(xxx)
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                
        b.addEventListener("click", function (e) {
            inp.value = this.getElementsByTagName("input")[0].value;
            window.location.replace("?stock=" + inp.value);            
        closeAllLists();
  
        });
        
      a.appendChild(b);
        }
    }
    if (val.length == 4 ) {
        if (arr[i].substr(0,4).toUpperCase().includes(val.toUpperCase()) & (count < 14))
            {
                count++;
                b = document.createElement("DIV");
                b.setAttribute("class","d-flex")
                xxx = document.createElement("div");
                xxx.setAttribute("class", "tickerCompany")
                xxx.innerHTML = arr[i]
                // xxx += "<input type='submit' class='btn btn-xs ml-3 border-0 bg-light' value='+' id='button__submit__portfolio'>";
                // b.innerHTML = arr[i]
                b.appendChild(xxx)
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                var ticker = arr[i].split(' | ')
                
        b.addEventListener("click", function (e) {
            inp.value = this.getElementsByTagName("input")[0].value;
            window.location.replace("?stock=" + inp.value);            
        closeAllLists();

        });
        
      a.appendChild(b);
        }
    }
    if (val.length == 5 ) {
        if (arr[i].substr(0,5).toUpperCase().includes(val.toUpperCase()) & (count < 14))
            {
                count++;
                b = document.createElement("DIV");
                b.setAttribute("class","d-flex")
                xxx = document.createElement("div");
                xxx.setAttribute("class", "tickerCompany")
                xxx.innerHTML = arr[i]
                // xxx += "<input type='submit' class='btn btn-xs ml-3 border-0 bg-light' value='+' id='button__submit__portfolio'>";
                // b.innerHTML = arr[i]
                b.appendChild(xxx)
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                var ticker = arr[i].split(' | ')
               
        b.addEventListener("click", function (e) {
            inp.value = this.getElementsByTagName("input")[0].value;
            window.location.replace("?stock=" + inp.value);            
        closeAllLists();

        });

        
      a.appendChild(b);
        }
    }
    if (val.length == 6 ) {
        if (arr[i].substr(0,6).toUpperCase().includes(val.toUpperCase()) & (count < 14))
            {
                count++;
                b = document.createElement("DIV");
                b.setAttribute("class","d-flex")
                xxx = document.createElement("div");
                xxx.setAttribute("class", "tickerCompany")
                xxx.innerHTML = arr[i]
                // xxx += "<input type='submit' class='btn btn-xs ml-3 border-0 bg-light' value='+' id='button__submit__portfolio'>";
                // b.innerHTML = arr[i]
                b.appendChild(xxx)
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                var ticker = arr[i].split(' | ')
                
        b.addEventListener("click", function (e) {
            inp.value = this.getElementsByTagName("input")[0].value;
            window.location.replace("?stock=" + inp.value);            
        closeAllLists();

        
        });
        
      a.appendChild(b);
        }
    }
    
    
    if (val.length > 6 ) {
        if (arr[i].substr(6,).toUpperCase().includes(val.toUpperCase()) & (count < 14))
            {
                count++;
                b = document.createElement("DIV");
                b.setAttribute("class","d-flex")
                xxx = document.createElement("div");
                xxx.setAttribute("class", "tickerCompany")
                xxx.innerHTML = arr[i]
                // xxx += "<input type='submit' class='btn btn-xs ml-3 border-0 bg-light' value='+' id='button__submit__portfolio'>";
                // b.innerHTML = arr[i]
                b.appendChild(xxx)
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                var ticker = arr[i].split(' | ')
                
        b.addEventListener("click", function (e) {
            inp.value = this.getElementsByTagName("input")[0].value;
            window.location.replace("?stock=" + inp.value);            
        closeAllLists();

        });
        
        
      a.appendChild(b);
        }
    }
  
    
    
    
    }
    });
    function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
    if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
    }
    }
    
    /*execute a function when someone clicks in the document:*/
    document.addEventListener("click", function (e) {
    // closeAllLists(e.target);
    });
    }
    
    
    
    /*initiate the autocomplete function on the "myInput" element, and pass along the countries array as possible autocomplete values:*/
    autocomplete(document.getElementById("autocomplete"), countries);
    }catch(err) {
    console.log(err);
    } 
    };
    allCompany('/allcompany');
});





