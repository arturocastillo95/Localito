const searchBar = document.getElementById('searchBar');
const menuItemsNodes = document.querySelectorAll('.menu-item');

const menuItems = Array.from(menuItemsNodes);

function searchItem (i) {
    const searchValue = i.target.value.toLowerCase();

    for (var i=0; i < menuItems.length;i++) {
        const item = menuItems[i];
        const itemString = item.innerText.toLowerCase();
        const element = document.getElementById(item.id);

        if (!itemString.includes(searchValue)) {
            element.classList.add('is-hidden')
        } else {
            element.classList.remove('is-hidden')
        };
    };
};

function allVisible () {
    for (var i=0; i < menuItems.length;i++) {
        const item = menuItems[i];
        const element = document.getElementById(item.id);
        element.classList.remove('is-hidden')
    };
};

searchBar.addEventListener('keyup', searchItem);
    function emptySearchBar () {
        searchBar.value = '';
        allVisible();
 };

 function collapseMenu (sectionId) {
    const element = document.getElementsByClassName(sectionId)[0];
    const hidden = 'item-is-colapsed';
    
    if (element.classList.contains(hidden)) {
        element.classList.remove(hidden)
        const icon = document.getElementById(sectionId).getElementsByClassName('fa-caret-left')[0];
        changeCollapseIcon(icon, 'fa-caret-down', 'fa-caret-left');
    } else {
        element.classList.add(hidden)
        const icon = document.getElementById(sectionId).getElementsByClassName('fa-caret-down')[0];
        changeCollapseIcon(icon, 'fa-caret-left', 'fa-caret-down');
    }
 };

 function changeCollapseIcon (iconElement, newIcon, oldIcon) {
    iconElement.classList.remove(oldIcon)
    iconElement.classList.add(newIcon)
 }


