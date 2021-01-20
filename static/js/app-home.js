let txt_municipality = ''
let txt_category = ''
window.onload = function () {
    document.getElementById('preloader').style.display = 'none'
}
document.addEventListener('DOMContentLoaded', function () {
    // Initialize
    let elems = document.querySelectorAll('select');
    let instances = M.FormSelect.init(elems);
    let categories = document.querySelectorAll('[data-role="category"]')
    let arrow_back = document.querySelector('.back-categories')
    let searchers = document.querySelectorAll('[searcher]')
    let btn_search = document.querySelector('#btn-search')
    let input_search = document.querySelector('#search')
    let backToTopButton = document.querySelector(".scrolltotop");
    backToTopButton.style.display = 'none'
    // Search with enter key
    input_search.addEventListener('keydown', function (e) {
        if (event.which == 13 || event.keyCode == 13) {
            if (this.value.trim().length > 0) {
                let municipality = document.querySelector('#id_municipios')
                txt_municipality = municipality.options[municipality.selectedIndex].text
                txt_category = input_search.value
                getData(null, null, name = input_search.value.trim(), municipality.value)
            }
        }
    })
    // Search with button search
    btn_search.addEventListener('click', function () {
        if (input_search.value.trim().length > 0) {
            let municipality = document.querySelector('#id_municipios')
            txt_municipality = municipality.options[municipality.selectedIndex].text
            txt_category = input_search.value
            getData(null, null, name = input_search.value.trim(), municipality.value)
        }
    })
    categories.forEach(element => {
        element.addEventListener('click', function () {
            let name = element.dataset.name
            let codename = element.dataset.codename
            let subcategories = document.querySelectorAll(`[data-parent-codename="${codename}"][data-role="subcategory"]`)
            let categories = document.querySelectorAll('[data-role="category"]')
            let title_categories = document.querySelector('.title-categories')
            title_categories.textContent = name
            arrow_back.style.display = 'block'
            // Hide categories
            categories.forEach(element => {
                element.style.display = 'none'
            })
            // Show subcategories
            subcategories.forEach((element, i) => {
                element.style.display = 'block'
                element.classList.add('animated', 'fadeIn')
                element.style.animationDuration = '600ms'
                element.style.animationDelay = `${(i + 1)}00ms`
            })
            // Add event to arrawback
            arrow_back.addEventListener('click', function () {
                cleanRenderedData()
                title_categories.textContent = 'O navega a través de nuestras categorías'
                subcategories.forEach(element => {
                    element.style.display = 'none'
                });
                categories.forEach((element, i) => {
                    element.style.display = 'block'
                    element.classList.add('animated', 'fadeIn')
                    element.style.animationDuration = '600ms'
                    element.style.animationDelay = `${(i + 1)}00ms`
                })
                this.style.display = 'none'
            })
        })
    })
    // Add event ajax to search results
    searchers.forEach(element => {
        element.addEventListener('click', function () {
            let municipality = document.querySelector('#id_municipios')
            txt_municipality = municipality.options[municipality.selectedIndex].text
            txt_category = element.dataset.name
            getData(codename = this.dataset.codename, null, null, municipality.value)
        })
    })

    // scrolltotop button
    window.addEventListener("scroll", function () {
        if (window.pageYOffset > 300) { // Show backToTopButton
            backToTopButton.style.display = "block";
        }
        else { // Hide backToTopButton
            backToTopButton.style.display = "none";
        }
    });
    backToTopButton.addEventListener("click", smoothScrollBackToTop);
    function smoothScrollBackToTop() {
        const targetPosition = 0;
        const startPosition = window.pageYOffset;
        const distance = targetPosition - startPosition;
        const duration = 750;
        let start = null;

        window.requestAnimationFrame(step);

        function step(timestamp) {
            if (!start) start = timestamp;
            const progress = timestamp - start;
            window.scrollTo(0, easeInOutCubic(progress, startPosition, distance, duration));
            if (progress < duration) window.requestAnimationFrame(step);
        }
    }
    function easeInOutCubic(t, b, c, d) {
        t /= d / 2;
        if (t < 1) return c / 2 * t * t * t + b;
        t -= 2;
        return c / 2 * (t * t * t + 2) + b;
    };
})

function getData(codename = null, page = null, name = null, municipality = null) {
    loader = document.getElementById('preloader')
    loader.style.display = 'block'
    axios({
        url: '/search',
        params: {
            cat: codename,
            page: page,
            name: name,
            municipios: municipality
        },
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
    }).then(function (response) {
        if (response.status == 200) {
            renderData(response.data)
        }
    }).catch(function (err) {
        console.log(err);
    }).then(function () {
        loader.style.display = 'none'
    });
}

function renderData(data) {
    cleanRenderedData()
    let cont_results = document.querySelector('.cont-results')
    cont_results.querySelector('h4').style.display = 'block'
    txt_result = cont_results.querySelector('h6')
    txt_result.innerHTML = `Para <b>${txt_category}</b> en <b>${txt_municipality}</b>`
    txt_result.style.display = 'block'
    if (data.length > 0) {
        data.forEach(element => {
            // create card-panel
            card_panel = document.createElement('div')
            card_panel.className = 'card-panel'
            // create row
            row = document.createElement('div')
            row.className = 'row card-row'
            // create first col
            col1 = document.createElement('div')
            col1.className = 'col l4 m12 s12'
            // create second col
            col2 = document.createElement('div')
            col2.className = 'col l4 m12 s12'
            // create third col
            col3 = document.createElement('div')
            col3.className = 'col l4 m12 s12 v-border'
            // --- 1st.
            // create img from first col
            img = document.createElement('img')
            img.src = element.logo
            img.className = 'responsive-img'
            // --- 2nd.
            // create h5 from second col
            h5 = document.createElement('h5')
            h5.textContent = element.name
            // create h6 from second col
            h6 = document.createElement('h6')
            h6.textContent = element.phonenumber
            // create h6 town from second col
            h6_town = document.createElement('h6')
            h6_town.textContent = element.municipality
            // create icono facebook
            face_ico = document.createElement('i')
            face_ico.className = 'fab fa-facebook-square fa-2x'
            aface = document.createElement('a')
            aface.href = element.facebook_url
            aface.target = '__blank'
            aface.appendChild(face_ico)
            // create icono whatsapp
            whats_ico = document.createElement('i')
            whats_ico.className = 'fab fa-whatsapp-square fa-2x'
            awhats = document.createElement('a')
            awhats.href = `https://wa.me/52${element.phonenumber}`
            awhats.target = '__blank'
            awhats.appendChild(whats_ico)
            // create icono instagram
            insta_ico = document.createElement('i')
            insta_ico.className = 'fab fa-instagram-square fa-2x'
            ainsta = document.createElement('a')
            ainsta.href = element.instagram_url
            ainsta.target = '__blank'
            ainsta.appendChild(insta_ico)
            // create web page icon
            web_ico = document.createElement('i')
            web_ico.className = 'fas fa-globe fa-2x webpage'
            aweb = document.createElement('a')
            aweb.href = element.web_url
            aweb.target = '__blank'
            aweb.appendChild(web_ico)


            // Put img into col 1
            col1.appendChild(img)
            // Put h5, h6 into col2
            col2.appendChild(h5)
            col2.appendChild(h6_town)
            col2.appendChild(h6)
            if (element.web_url != null) {
                col2.appendChild(aweb)
            }
            if (element.facebook_url != null) {
                col2.appendChild(aface)
            }
            if (element.phonenumber != null) {
                col2.appendChild(awhats)
            }
            if (element.instagram_url != null) {
                col2.appendChild(ainsta)
            }
            // Put dealers into col 3
            if (element.own_service) {
                service_txt = document.createElement('h6')
                b = document.createElement('b')
                b.textContent = 'Servicio a domicilio propio'
                service_txt.appendChild(b)
                col3.appendChild(service_txt)
            }
            else {
                element.dealers.forEach(element => {
                    img = document.createElement('img')
                    a = document.createElement('a')
                    if (element.app_url) {
                        a.href = element.app_url
                    }
                    else if (element.phonenumber) {
                        a.href = `https://wa.me/52${element.phonenumber}`
                    }
                    else {
                        a.href = ""
                    }
                    a.target = '__blank'
                    img.src = element.logo
                    img.className = 'logo-dealer z-depth-1'
                    a.appendChild(img)
                    col3.appendChild(a)
                });
            }
            // Put col1, col2, col3 into row
            row.appendChild(col1)
            row.appendChild(col2)
            row.appendChild(col3)
            // Put row into card-panel
            card_panel.appendChild(row)
            // Put card-panel into cont_results
            cont_results.appendChild(card_panel)
        });
    }
    else {
        // create card-panel
        card_panel = document.createElement('div')
        card_panel.className = 'card-panel'
        // create h5
        h5 = document.createElement('h5')
        h5.textContent = 'No se encontraron resultados'
        h5.className = 'center-align'
        // Put h5 into card-panel
        card_panel.appendChild(h5)
        // Put card-panel into cont_results
        cont_results.appendChild(card_panel)
    }
    cont_results.scrollIntoView({
        behavior: 'smooth'
    });
}

function cleanRenderedData() {
    let cont_results = document.querySelector('.cont-results')
    cont_results.querySelector('h4').style.display = 'none'
    cont_results.querySelector('h6').style.display = 'none'
    let cards = cont_results.querySelectorAll('.cont-results .card-panel')
    cards.forEach(element => {
        element.remove()
    });
}