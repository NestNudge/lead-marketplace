// Safe autocomplete
function initAutocomplete() {
  try {
    const input = document.getElementById("address");

    if (!input || typeof google === "undefined") return;

    if (google.maps.places.Autocomplete) {
      const autocomplete = new google.maps.places.Autocomplete(input);

      autocomplete.addListener("place_changed", () => {
        const place = autocomplete.getPlace();
        if (place && place.formatted_address) {
          input.value = place.formatted_address;
        }
      });
    }

  } catch (err) {
    console.warn("Autocomplete failed:", err);
  }
}

// Submit form
document.addEventListener("DOMContentLoaded", () => {
  initAutocomplete();

  const form = document.getElementById("leadForm");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
      address: document.getElementById("address").value,
      projectType: document.getElementById("projectType").value,
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      phone: document.getElementById("phone").value
    };

    const res = await fetch("https://nestnudge-api.onrender.com/submit-lead", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    if (res.ok) {
      alert("Success!");
    } else {
      alert("Error submitting lead");
    }
  });
});
