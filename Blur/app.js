const observerblur = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if(entry.isIntersecting){
            entry.target.classList.add('show');
        } else {
            entry.target.classList.remove('show');
        }
    });
});

const observerfixed = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        console.log(entry)
        if(entry.isIntersecting){
            entry.target.classList.add('fixed');
        } else {
            entry.target.classList.remove('fixed');
        }
    });
});

const hiddenElements = document.querySelectorAll('.hidden')

hiddenElements.forEach((el)=>observerblur.observe(el));
const hiddenElements2 = document.querySelectorAll('.hidden-delay-right')

hiddenElements2.forEach((el)=>observerblur.observe(el));

const unfixedElements = document.querySelectorAll('.unfixed')

unfixedElements.forEach((el)=>observerblur.observe(el));