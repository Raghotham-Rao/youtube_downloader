function setActiveLink(i){
    $('ul.navbar-nav').find('li.active').removeClass('active');
    $('ul.navbar-nav>li').get(i).setAttribute('class', 'list-item active');
}