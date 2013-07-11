function replace(s) {
    var from = s
    var to = $('#principal')

    var from_ = from.clone(true)
    var to_ = to.clone(true)

    from_.attr('id', 'principal')
    to_.removeAttr('id')

    from.replaceWith(to_)
    to.replaceWith(from_)
};

function load(html) {
    $('.square:not(#principal)').each(function(k,v) {
        t = $(this)
        t.html(html[k])
    });
};
