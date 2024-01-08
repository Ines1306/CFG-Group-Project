backend_url = 'http://127.0.0.1:5005/thrilltopia/';

const getAllActivities = () => {
    return fetch(`${backend_url}activities`, {
        method: 'GET',
    });
}

const addAReservation = (data) => {
    const response = fetch(`${backend_url}reservations`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
    });
    return response;
}

const checkWeather = (id, date, time) => {
    const response = fetch(`${backend_url}weather/${id}/${date}/${time}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json' }
    });
    return response;
}

// create an activity card and populate it with data
const getCard = (parent, id, image_url, title_text, outdoor, description, price, duration) => {
    const card = `
    <div class="col-3">
        <div class="card" style="width: 18rem;">
            <img src="${image_url}" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">${title_text}</h5>
                <p class="card-text">${description}</p>
                  <ul class="list-group list-group-flush">
                    <li class="list-group-item">price: €${price}</li>
                    <li class="list-group-item">duration: ${duration}</li>
                  </ul>
                <a href="#" class="btn btn-info" id="form-btn-${id}" data-bs-toggle="modal" data-bs-target="#staticBackdrop">Check availability</a>
            </div>
        </div>
    </div>
    `;

    parent.insertAdjacentHTML('beforeend', card);
    document.getElementById(`form-btn-${id}`).addEventListener('click', () => populateModal(id, title_text, outdoor));
}

// handle making a reservation and displaying the outcome
const reservationHandler = () => {
    const id = document.getElementById("form-submit-btn").getAttribute('act-id');
    const [firstName, lastName, phoneNumber, date, time, numberOfPeople] = reservationData();
    const data = {
        first_name: firstName,
        last_name: lastName,
        phone_number: phoneNumber,
        reservation_date: date,
        reservation_time: time,
        num_of_people: numberOfPeople,
        activity_id: id,
        equipment_id: id
    };
    addAReservation(data).then((res) => {
        if (res.ok) {
            document.getElementById('modal-body').style.display = 'none';
            document.getElementById('alert-container').innerHTML = `
            <div class="alert alert-info" role="alert">
                Reservation made successfully!
            </div>`;
        } else {
            document.getElementById('modal-body').style.display = 'none';
            document.getElementById('alert-container').innerHTML = `
            <div class="alert alert-danger" role="alert">
                Couldn't make a reservation, please contact us directly.
            </div>`;
        }
    })
}

// asynchronously check the weather and display the outcome
const checkAvaliability = async (id, outdoor) => {
    document.getElementById('form-submit-btn').setAttribute('disabled', '');
    const { 3: date, 4: time } = reservationData();
    if (outdoor == 1) {
        await checkWeather(id, date, time)
            .then((res) => res.json())
            .then((jsonRes) => {
                document.getElementById('info-container').innerHTML = `
                <p>${jsonRes}<p/>
                <p id="weather-p">If you wish to continue with the reservation, click the button below.</p>`;
            })
    } else {
        document.getElementById('info-container').innerHTML = `
        <p id="weather-p">Reservation is available. Please confirm by clicking on the button below.</p>`;
    }
    document.getElementById('weather-p').insertAdjacentHTML('afterend', `
        <button type="button" id="make-reservation-btn" class="btn btn-info">Make a reservation</button>`);
    document.getElementById('make-reservation-btn').addEventListener('click', reservationHandler);
}

// poplulate the reservation form modal
const populateModal = (id, activity_name, outdoor) => {
    document.getElementById('staticBackdropLabel').innerText = activity_name;
    const form = document.getElementById('form-id');
    const formSubButton = document.getElementById('form-submit-btn');
    formSubButton.setAttribute('act-id', id);
    formSubButton.setAttribute('act-out', outdoor);
    formSubButton.addEventListener('click', submitHandler);
}

// handle the form submit button
const submitHandler = () => {
    const form = document.getElementById('form-id');
    const submitBtn = document.getElementById("form-submit-btn");
    const id = submitBtn.getAttribute('act-id');
    const outdoor = submitBtn.getAttribute('act-out');
    if (form.checkValidity()) {
        checkAvaliability(id, outdoor)
    }
}

// get all the activities and call getCard function passing the data
getAllActivities().then(res => res.json())
    .then(jsonRes => jsonRes.forEach(obj => {
        getCard(
            document.getElementById('card-container'),
            obj['Activity id'],
            obj['Photo URL'],
            obj['Activity Name'],
            obj['Indoor / Outdoor'],
            obj['Activity Description'],
            obj['Price'],
            obj['Duration']
        )
    }));

// reset the reservation form modal after clicking 'close' or 'x'
const resetForm = () => {
    document.getElementById('modal-body').style.display = 'block';
    document.getElementById('form-id').reset();
    makeReservationBtn = document.getElementById('make-reservation-btn')
    if (makeReservationBtn){
        makeReservationBtn.removeEventListener('click', reservationHandler);
    }
    document.getElementById('info-container').innerHTML = '';
    document.getElementById('form-submit-btn').removeEventListener('click', submitHandler);
    document.getElementById('form-submit-btn').removeAttribute('disabled');
    document.getElementById('alert-container').innerHTML = '';
}

// parse the dates that are displayed in the date input
const getDates = () => {
    const timeElapsed = Date.now();
    const today = new Date(timeElapsed);
    const currentDate = today.toISOString().split('T')[0];

    const todayPlus15Days = new Date(today);
    todayPlus15Days.setDate(today.getDate() + 14);
    const maxDate = todayPlus15Days.toISOString().split('T')[0];
    return [currentDate, maxDate];
}

// get the data from reservation form
const reservationData = () => {
    const firstName = document.getElementById("inputFirstName").value;
    const lastName = document.getElementById("inputLastName").value;
    const phoneNumber = document.getElementById("inputPhone").value;
    const date = document.getElementById("inputDate").value;
    const time = document.getElementById("inputTime").value;
    const numberOfPeople = document.getElementById("inputPeople").value;
    return [firstName, lastName, phoneNumber, date, time, numberOfPeople];
}

// create reservation form
const reservationForm = () => {
    const [currentDate, maxDate] = getDates();
    const form = `
        <div class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header" id="modal-header">
                    <h1 class="modal-title fs-5" id="staticBackdropLabel">Reservation form</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" onclick="resetForm()"></button>
                    </div>
                    <div id="alert-container"></div>
                    <div class="modal-body" id="modal-body">
                        <form id="form-id" class="container">
                            <div class="mb-3">
                                <label for="firstName" class="form-label">First name</label>
                                <input type="text" class="form-control" id="inputFirstName" required>
                            </div>
                            <div class="mb-3">
                                <label for="lastName" class="form-label">Last name</label>
                                <input type="text" class="form-control" id="inputLastName" required>
                            </div>
                            <div class="mb-3">
                                <label for="phone" class="form-label">Phone number</label>
                                <input type="tel" class="form-control" id="inputPhone" required>
                            </div>
                            <div class="mb-3">
                                <label for="date" class="form-label">Pick a date</label>
                                <input type="date" class="form-control" id="inputDate" value="${currentDate}" min="${currentDate}" max="${maxDate}" required>
                            </div>
                            <div class="mb-3">
                                <label for="time" class="form-label">Choose starting time</label>
                                <input type="time" class="form-control" id="inputTime" min="10:00" max="18:00" required>
                            </div>
                                <label for="number" class="form-label">Number of people</label>
                                <input type="number" class="form-control" id="inputPeople" min="1" max="10" required>
                            <div class="modal-footer">
                                <button type="submit" id="form-submit-btn" class="btn btn-info">Check availability</button>
                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="close-btn" onclick="resetForm()">Close</button>
                            </div>
                            <div id="info-container"></div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    `;
    return form;
}
document.getElementById('form-stick').insertAdjacentHTML('afterend', reservationForm());

// toggle homepage content visibility
const homePage = () => {
    document.getElementById('card-container').style.display = 'flex';
    document.getElementById('about-container').style.display = 'none';
}

// create about us page content
const aboutUs = () => {
    const about = `
    <div class="col mb-3">
        <div class="card h-100" style="width: 18rem;">
            <img src="../static/ines_pic.jpg" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">Inês Branco Veiga</h5>
                <p class="card-text">Master's Degree in Management and a dog's mom 🐕 I am currently a digital product manager trying to switch to a more technical area 💻</p>
            </div>
        </div>
    </div>
    <div class="col mb-3">
        <div class="card h-100" style="width: 18rem;">
            <img src="../static/vicki_pic.png" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">Vicki Gibbison</h5>
                <p class="card-text">Career Switching Mum, graduated from university as a mature student 2022 with a Bachelor's Degree in Psychology 🤓 I then went onto complete a Software Engineering 16 week bootcamp with Sky called Get Into Tech.</p>
            </div>
        </div>
    </div>
    <div class="col mb-3">
        <div class="card h-100" style="width: 18rem;">
            <img src="../static/kayla_pic.jpg" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">Kayla Hong</h5>
                <p class="card-text">A dog Mum hoping to switch to Tech with my non-Tech background. Before this degree, I've completed Data & SQL Kickstarter with CFG.</p>
            </div>
        </div>
    </div>
    <div class="col mb-3">
        <div class="card h-100" style="width: 18rem;">
            <img src="../static/paula_pic.jpg" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">Paula Kuwałek</h5>
                <p class="card-text">Master's Degree in Law ⚖ career switcher to software engineering 💻 I did courses on web development, full stack with React and Node.js and Cloud Computing on AWS.</p>
            </div>
        </div>
    </div>
    <div class="col mb-3">
        <div class="card h-100" style="width: 18rem;">
            <img src="../static/sofia_pic.png" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">Sofia Leong</h5>
                <p class="card-text">Professional violinist with a Bachelor's Degree in Orchestra and a Master's Degree in Violin. Currently studying computer science at 42 Lisboa</p>
            </div>
        </div>
    </div>
    <div class="col mb-3">
        <div class="card h-100" style="width: 18rem;">
            <img src="../static/marnie_pic.jpg" class="card-img-top">
            <div class="card-body">
                <h5 class="card-title">Marnie Thomson</h5>
                <p class="card-text">A Secondary Geography Teacher with a background in Environmental Management. Earlier this year I did the Data & SQL kickstarter with CFG and was hooked 😎</p>
            </div>
        </div>
    </div>
    `;
    document.getElementById('about-container').insertAdjacentHTML('beforeend', about);
}

aboutUs();

// toggle about us page content visibility
const aboutUsPage = () => {
    document.getElementById('card-container').style.display = 'none';
    document.getElementById('about-container').style.display = 'flex';
}