function loadContent(page) {
  const mainContent = document.getElementById("main-content");

  switch (page) {
    case "manageVenue":
      mainContent.innerHTML = `
                <div class="form-container">
                <h1>Add Venue</h1>
                <form>
                    <div class="form-group">
                        <label for="room-number">Room number:</label>
                        <input type="text" id="room-number" name="room-number" required>
                    </div>
                    <div class="form-group">
                        <label for="seating-capacity">Seating Capacity:</label>
                        <input type="number" id="seating-capacity" name="seating-capacity" required>
                    </div>
                    <div class="form-group">
                        <label for="block-name">Block Name:</label>
                        <input type="text" id="block-name" name="block-name" required>
                    </div>
                    <div class="form-group">
                        <label for="address">Floor Number:</label>
                        <input type="text" id="floor-number" name="floor-number" required>
                    </div>
                    <div class="form-group">
                        <label for="room-type">Room Type:</label>
                        <select id="room-type" name="room-type" required>
                            <option value="">--Select Room--</option>
                            <option value="type1">Conference room</option>
                            <option value="type2">Training room</option>
                            <option value="type3">Auditorium</option>
                        </select>
                    </div>
                    <button type="submit" class="btn-submit">Submit</button>
                </form>
            </div>`;
      break;

    case "addBooking":
      mainContent.innerHTML = `
            <div class="form-container">
                <h1>Add Booking</h1>
                <form>
                <div class="form-group">
                <label for="booking-id">Booking ID:</label>
                <input type="text" id="booking-id" value="128" readonly>
                </div>
                
                <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" placeholder="Enter your name">
                </div>

                <div class="form-group">
                <label for="phone">Phone No:</label>
                <input type="text" id="phone" placeholder="Enter phone number">
                </div>

                <div class="form-group">
                <label for="email">Email ID:</label>
                <input type="email" id="email" placeholder="Enter email address">
                </div>
               

                <div class="form-group">
                <label for="venue">Venue:</label>
                <select id="venue">
                    <option value="" disabled selected>--Select--</option>
                    <option value="venue1">Venue 1</option>
                    <option value="venue2">Venue 2</option>
                </select>
                </div>


                <div class="form-group">
                <label for="purpose">Purpose:</label>
                <select id="purpose">
                    <option value="" disabled selected>--Select--</option>
                    <option value="marriage">Marriage</option>
                    <option value="engagement">Engagement</option>
                </select>
                </div>
                

                <div class="form-group">
                <label for="booking-type">Booking Type:</label>
                <select id="booking-type">
                    <option value="" disabled selected>--Select--</option>
                    <option value="full-day">Full Day</option>
                    <option value="first-half">First Half</option>
                    <option value="second-half">Second Half</option>
                </select>
                </div>
                

                <div class="form-group">
                <label for="booking-date">Booking Date:</label>
                <input type="date" id="booking-date">
                </div>

                <button type="submit" class="btn-submit">Submit</button>
                </form>
            </div>`;
      break;
    case "viewBooking":
      mainContent.innerHTML = `
                <h1>View Booking</h1>
                <p>Here, you can view all bookings.</p>
                <!-- Add functionality for viewing bookings -->
            `;
      break;
    case "cancelBooking":
      mainContent.innerHTML = `
                <h1>Cancel Booking</h1>
                <p>Here, you can cancel bookings.</p>
                <!-- Add functionality for canceling bookings -->
            `;
      break;

    default:
      mainContent.innerHTML = `<h1>Welcome to the Admin Panel</h1>`;
  }
}
window.onload = function () {
  loadContent("manageVenue");
};
