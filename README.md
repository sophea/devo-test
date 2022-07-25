
# Exercise 1 : 

###
## call from command line
#: python3 index.py classify 6
python3 index.py classify 6
sum divisors from 6 value is 6
6 is perfect number

$python3 index.py classify 28
sum divisors from 28 value is 28
28 is perfect number

$ python3 index.py classify 12
sum divisors from 12 value is 16
12 is abundant number

$python3 index.py classify 121
sum divisors from 121 value is 12
121 is deficient number



# Exercise 2 : 
Use chart.js library https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"

1 - line chart :  http://localhost:63342/devo-test/Exercise2/chart.html

### fetch all 3 JSONS files 
data1.json : http://s3.amazonaws.com/logtrust-static/test/test/data1.json
data2.json : http://s3.amazonaws.com/logtrust-static/test/test/data2.json
data3.json : http://s3.amazonaws.com/logtrust-static/test/test/data3.json

compile all json values into JS Object list of MyObject(cat, d, value)


//data1.json : parse date format from millisecond to date yyyy-mm-dd
````
/**format date yyyy-mm-dd*/
  function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2)
      month = '0' + month;
    if (day.length < 2)
      day = '0' + day;

    return [year, month, day].join('-');
  }
````

//data3.json : lookup for date and cat value
````
// parse Date value "CcoeoNR8 T4VSBd0GC fpAepuTD 5A40zJ6 y5bXBb rRxM 2015-06-08 J KA9FicdV BSbvirf #CAT 2#"
  function parseRawToDate(value) {
    result = value.split(/\d{4}-\d{2}-\d{2}/);
    var yyyyMMdd=''
    for(const item of result) {
      yyyyMMdd = value.replace(item,'')
      value = yyyyMMdd
   //   console.log(yyyyMMdd)
    }
    return yyyyMMdd;
  }

 // parseRawToDate(value)

  function parseRawCat(value) {
    result = value.split(/#/);
    for (const item of result) {
      if (item.startsWith("CAT")) {
        return item;
      }
     // console.log(item)
    }
  }
````
chart.js

populate to Category with unique as label
populate date as X lines
poulate value as Y lines

render chart.data.datasets with value object above and render it
````
////////////Chart Object
        var chart = new Chart("myChart", {
          type: "line",
          data: {
            labels: dateValues,
            datasets: []
          },
          options: {
            legend: {display: true},
            text: "Chart dashboard",
          }
        });
        //////////////add datasets to the chart
        var index = 0;
        for (const cat of categories) {
          var values = getValueByCat(cat, allItems, dateValues);
          var object1 = {
            label: cat,
            data: values,
            borderColor: COLORS[index++],
            fill: false
          }
          chart.data.datasets.push(object1);
        }
        //update chart to reflect the datasets
        chart.update()

````

2 - pie chart :  http://localhost:63342/devo-test/Exercise2/pie.html

similar as chart.html - merging all 3 json files into js list of Objects and render it is pie chart with Category as label 
and Group value with the same category
```
// get value by category
        function getTotalValueByCat(cat, items) {

          var total = 0
          for (const item of items) {
            const v = item.cat.toUpperCase();
            //category
            if (v == cat) {
               total += item.value
            }
          }
          return total;
        }
        
 ////////////Chart Object
        var chart = new Chart("myChart", {
          type: "pie",
          data: {
            labels: categories,
            datasets: [{
              backgroundColor: barColors,
              data: data,

            }]
          },
          options: {
            legend: {display: true},
            title: {
              display: true,
              text: "Categories"
            }
          }
        });
        //update chart to reflect the datasets
        chart.update()
```
