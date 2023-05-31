var nav = document.getElementById('nav');

window.onscroll = function() {
    if (window.pageYOffset > 100) {
      nav.classList.add('scrolling');
    } else {
      nav.classList.remove('scrolling');
    }
};
        

// Zugriff auf das Datepicker-Element
var datePicker = document.getElementById('checkin');
var datePicker2 = document.getElementById('checkout');

// Zugriff auf das Display-Element
var displayDate = document.getElementById('displaycheckin');
var displayDate2 = document.getElementById('displaycheckout');

// Definieren Sie den Event-Handler für das 'input'-Event
datePicker.addEventListener('input', function(event) {
    if (event.target.value) {
      // Erstellen Sie ein neues Date-Objekt aus dem Wert des Datepicker-Elements
      var date = new Date(event.target.value);
  
      // Formatieren Sie das Datum
      var day = String(date.getDate()).padStart(2, '0');
      var month = String(date.getMonth() + 1).padStart(2, '0'); // Monate sind von 0-11
      var year = date.getFullYear();
  
      var formattedDate = day + '.' + month + '.' + year;
  
      // Zeigen Sie das formatierte Datum im Display-Element an
      displayDate.textContent = formattedDate;
    } else {
      displayDate.textContent = 'Check In';
    }
});

// Überprüfen Sie den anfänglichen Zustand des Datepicker-Elements
if (datePicker.value) {
  displayDate.textContent = datePicker.value;
} else {
  displayDate.textContent = 'Check In';
}

// Definieren Sie den Event-Handler für das 'input'-Event
datePicker2.addEventListener('input', function(event) {
    if (event.target.value) {
      // Erstellen Sie ein neues Date-Objekt aus dem Wert des Datepicker-Elements
      var date = new Date(event.target.value);
  
      // Formatieren Sie das Datum
      var day = String(date.getDate()).padStart(2, '0');
      var month = String(date.getMonth() + 1).padStart(2, '0'); // Monate sind von 0-11
      var year = date.getFullYear();
  
      var formattedDate = day + '.' + month + '.' + year;
  
      // Zeigen Sie das formatierte Datum im Display-Element an
      displayDate2.textContent = formattedDate;
    } else {
      displayDate2.textContent = 'Check In';
    }
  });

// Überprüfen Sie den anfänglichen Zustand des Datepicker-Elements
if (datePicker2.value) {
    displayDate2.textContent = datePicker2.value;
} else {
    displayDate2.textContent = 'Check Out';
}

function openModalGuests() {
    var guestModal = document.getElementById('guest');
    var adultCounter = document.getElementById('countadults');
    var childrenCounter = document.getElementById('countchildren');
    var guestDisplay = document.getElementById('guestdisplay');
    var confirmButton = document.getElementById('confirmButton');

    // Modal öffnen
    guestModal.style.display = 'block';

    // Event-Handler für die Bestätigungsschaltfläche
    confirmButton.addEventListener('click', function() {
        var adultCount = adultCounter.value;
        var childrenCount = childrenCounter.value;

        if (adultCount == 0 && childrenCount == 0) {
            guestDisplay.textContent = 'Gäste';
        } else {
            guestDisplay.textContent = 'Erwachsene: ' + adultCount + ', Kinder: ' + childrenCount;
        }
        // Modal schließen
        guestModal.style.display = 'none';
    });
}

function openModalAirports() {
  var airportsModal = document.getElementById('airports');
  var airportDisplay = document.getElementById('outbounddepartureairport');
  var airportDisplay2 = document.getElementById('airportDisplay2');
  var confirmButton = document.getElementById('confirmButton2');
  var airportSelect = document.getElementById('airportSelect');

  // Modal öffnen
  airportsModal.style.display = 'block';

  // Event-Handler für die Bestätigungsschaltfläche
  confirmButton.addEventListener('click', function() {
      airportValue = airportSelect.value

      if (airportValue == 'NOT') {
          airportDisplay2.textContent = 'Flughafen';
      } else {
          // Werte in guestdisplay anzeigen
          airportDisplay2.textContent = airportValue;
      }
      airportDisplay.value = airportValue;

      // Modal schließen
      airportsModal.style.display = 'none';
  });
}

