function toggleWishlist(event, item_id) {
    event.preventDefault();
    const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
     fetch(`/wishlist/toggle/${item_id}/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken
            },
        })
        .then(response => response.json())
        .then(data => {
            const icon = document.querySelector(`#wishlist-icon-${item_id}`);
            const link = document.querySelector(`#wishlist-link-${item_id}`);
             if (data.action === "add") {
                icon.classList.remove("far");
                icon.classList.add("fas");
                link.setAttribute("onclick", `toggleWishlist(event, ${item_id})`);
            } else {
                icon.classList.remove("fas");
                icon.classList.add("far");
                link.setAttribute("onclick", `toggleWishlist(event, ${item_id})`);
            }
        });
}