function sortTable(n) {
  var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
  table = document.getElementById("myTable");
  switching = true;
  dir = "asc";

  while (switching) {
    switching = false;
    rows = table.rows;

    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("TD")[n];
      y = rows[i + 1].getElementsByTagName("TD")[n];

      // Parse the content as integers for the Priority column
      if (n === 2) { // Assuming Priority is the 3rd column (index 2)
        x = parseInt(x.innerHTML);
        y = parseInt(y.innerHTML);
      } else {
        x = x.innerHTML.toLowerCase();
        y = y.innerHTML.toLowerCase();
      }

      if (dir == "asc") {
        if (x > y) {
          shouldSwitch = true;
          break;
        }
      } else if (dir == "desc") {
        if (x < y) {
          shouldSwitch = true;
          break;
        }
      }
    }

    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
      switchcount++;
    } else {
      if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }
}




function changePerPage(select) {
  const perPage = select.value;
  const url = new URL(window.location.href);
  url.searchParams.set('per_page', perPage);
  window.location.href = url.toString();
}
