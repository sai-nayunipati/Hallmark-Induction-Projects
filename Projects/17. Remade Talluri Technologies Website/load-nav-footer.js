// Load the navbar.
$("#navbar").load("templates/navbar.html", () => {
// Update the navbar to make the relevant link active. 
var url = window.location.href.split('/')
var loc = url[url.length - 1]
// Ignore any "scroll-to" commands.
loc = loc.split("#")[0]

// If statement in case the link is in a dropdown.
let linkHolder = $('a[href$="' + loc + '"]')
if (linkHolder.hasClass('nav-link')) {
    $('a[href$="' + loc + '"]').addClass('active')
}
else {
    $('a[href$="' + loc + '"]').parent().parent().siblings().addClass('active')
}
});

// Load the footer.
$("#footer").load("templates/footer.html");