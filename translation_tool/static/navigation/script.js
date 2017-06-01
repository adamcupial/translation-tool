class Navigation extends window.HTMLElement {

  _addListeners() {
    this.addEventListener('click', this._onClick);
  }

  attachedCallback() {
    this._onClick = this._onClick.bind(this);
    this.links = this.querySelectorAll('nav-link');
    this._addListeners();
  }

  _onClick(evt) {
    const link = evt.target;
    evt.preventDefault();

    if (link.active)
      return;

    window.history.pushState({}, link.title, link.href);
    this.links.forEach(lnk => {
      if (lnk === link) {
        lnk.setAttribute('active', '');
      } else {
        lnk.removeAttribute('active');
      }
    });
  }

}

class NavLink extends window.HTMLElement {
  get href() {
    return this.getAttribute('href');
  }

  get title() {
    return this.innerText;
  }

  get active() {
    return this.getAttribute('active') || false;
  }
}

document.registerElement('nav-link', NavLink);
document.registerElement('nav-container', Navigation);
