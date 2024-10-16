$(document).ready(() => {
    const searchInput = $('#search-input');
    const searchResults = $('#search-results');
    let timer;

    searchInput.on('input', () => {
        clearTimeout(timer);
        const query = searchInput.val();

        timer = setTimeout(() => {
            if (query.length > 1) {
                $.ajax({
                    url: '/api/vendors-search',
                    data: { query },
                    success(data) {
                        searchResults.empty();
                        data.forEach(vendor => {
                            searchResults.append(
                                `<li class="list-group-item" data-id="${vendor.id}">
                                    <a href="/vendors/${vendor.id}" class="stretched-link">${vendor.name}</a>
                                </li>`
                            );
                        });
                    }
                });
            } else {
                searchResults.empty();
            }
        }, 300);
    });


    let customSlideIndex = 0;

function moveSlide(n) {
  const items = document.querySelectorAll('.custom-carousel-item');
  customSlideIndex += n;

  if (customSlideIndex >= items.length) {
    customSlideIndex = 0;
  } else if (customSlideIndex < 0) {
    customSlideIndex = items.length - 1;
  }

  const offset = -customSlideIndex * 100;
  document.querySelector('.custom-carousel-inner').style.transform = `translateX(${offset}%)`;
}

// Auto-slide
setInterval(() => moveSlide(1), 3000);

});
