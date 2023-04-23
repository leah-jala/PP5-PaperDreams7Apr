document.addEventListener("DOMContentLoaded", function () {
    const postLinks = document.querySelectorAll(".tutorial-post-link");
    const weekPosts = document.querySelectorAll(".week-post");

    // Show the first week by default
    if (weekPosts.length > 0) {
        weekPosts[0].style.display = "block";
    }

    // Add the 'active' class to the first link by default
    if (postLinks.length > 0) {
        postLinks[0].classList.add("active");
    }

    postLinks.forEach(link => {
        link.addEventListener("click", event => {
            event.preventDefault();
            const weekNumber = link.dataset.week;

            // Remove the 'active' class from all the links
            postLinks.forEach(link => link.classList.remove("active"));

            // Add the 'active' class to the clicked link
            event.target.classList.add("active");

            weekPosts.forEach(post => {
                if (post.id === `week-${weekNumber}`) {
                    post.style.display = "block";
                } else {
                    post.style.display = "none";
                }
            });
        });
    });
});