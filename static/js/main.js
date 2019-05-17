function submitform() {
    document.form_search.submit();
}

function focus_input() {
    document.getElementById("search_bar").classList.add("fcus");
}

function onblur_input() {
    document.getElementById("search_bar").classList.remove("fcus");
}