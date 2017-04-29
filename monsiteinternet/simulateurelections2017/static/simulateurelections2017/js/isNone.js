   function toggleDisplay() {
        // var x = document.getElementsByClassName('isNone');
        // console.log(x);
        // if (x.style.display === 'none') {
        //     x.style.display = 'block';
        // } else {
        //     x.style.display = 'none';
        // }
        var x = document.getElementById("mp"); // Using a class instead, see note below.
        x.classList.toggle('isNone');
        var x = document.getElementById("em"); // Using a class instead, see note below.
        x.classList.toggle('isNone');
    }

