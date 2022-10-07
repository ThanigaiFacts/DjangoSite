function actionChanged(){
        //var selectElement = event.target;
        //var value = selectElement.value;
        var x = document.getElementById("CompanyList")
        var y = document.getElementById("CompName")
        var z = document.getElementById("actionListID")
        if (z.value == "Buy")
         {
          var option = document.createElement("option")
          option.text = "Other"
          option.value = "Other"
          x.add(option,x[0])
          x.selectedIndex = "0";
          y.value = "";
          document.getElementById("CompName").focus();
        }
        else{
        if (x.options[0].value == "Other")
        {
         x.remove(0);
        }
        companyListChanged();
        }

}
function companyListChanged(){
  var x = document.getElementById("CompanyList")
  var y = document.getElementById("CompName")
  if(x[x.selectedIndex].value == "Other")
  {
   y.value = "";
   document.getElementById("CompName").focus();
  }
  else{
     y.value = x[x.selectedIndex].value;
     document.getElementById("buyPrice").focus();
  }


}

function checkNum(event){
   return (event.keyCode >= 48 && event.keyCode <= 57) || (event.keyCode == 46);
}

function checkInt(event){
  return (event.keyCode >= 48 && event.keyCode <= 57)
}
actionChanged();


