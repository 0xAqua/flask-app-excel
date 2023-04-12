function calc1() {
  let num1_1 = document.getElementById("quantity__1").value;
  let num1_2 = document.getElementById("unit__price__1").value;

  let res1 = num1_1 * num1_2;

  document.getElementById("amount__1").value = res1;
}

function calc2() {
  let num2_1 = document.getElementById("quantity__2").value;
  let num2_2 = document.getElementById("unit__price__2").value;

  let res2 = num2_1 * num2_2;

  document.getElementById("amount__2").value = res2;
}

function calc3() {
  let num3_1 = document.getElementById("quantity__3").value;
  let num3_2 = document.getElementById("unit__price__3").value;

  let res3 = num3_1 * num3_2;

  document.getElementById("amount__3").value = res3;
}

function calc4() {
  let num4_1 = document.getElementById("quantity__4").value;
  let num4_2 = document.getElementById("unit__price__4").value;

  let res4 = num4_1 * num4_2;

  document.getElementById("amount__4").value = res4;
}

function calc5() {
  let num5_1 = document.getElementById("quantity__5").value;
  let num5_2 = document.getElementById("unit__price__5").value;

  let res5 = num5_1 * num5_2;

  document.getElementById("amount__5").value = res5;
}

function calc6() {
  let num6_1 = document.getElementById("quantity__6").value;
  let num6_2 = document.getElementById("unit__price__6").value;

  let res6 = num6_1 * num6_2;

  document.getElementById("amount__6").value = res6;
}

function calc7() {
  let num7_1 = document.getElementById("quantity__7").value;
  let num7_2 = document.getElementById("unit__price__7").value;

  let res7 = num7_1 * num7_2;

  document.getElementById("amount__7").value = res7;
}

function calc8() {
  let num8_1 = document.getElementById("quantity__8").value;
  let num8_2 = document.getElementById("unit__price__8").value;

  let res8 = num8_1 * num8_2;

  document.getElementById("amount__8").value = res8;
}

function calc9() {
  let num9_1 = document.getElementById("quantity__9").value;
  let num9_2 = document.getElementById("unit__price__9").value;

  let res9 = num9_1 * num9_2;

  document.getElementById("amount__9").value = res9;
}

function calc10() {
  let num10_1 = document.getElementById("quantity__10").value;
  let num10_2 = document.getElementById("unit__price__10").value;

  let res10 = num10_1 * num10_2;

  document.getElementById("amount__10").value = res10;
}

function calc11() {
  let num11_1 = document.getElementById("quantity__11").value;
  let num11_2 = document.getElementById("unit__price__11").value;

  let res11 = num11_1 * num11_2;

  document.getElementById("amount__11").value = res11;
}

function calc12() {
  let num12_1 = document.getElementById("quantity__12").value;
  let num12_2 = document.getElementById("unit__price__12").value;

  let res12 = num12_1 * num12_2;

  document.getElementById("amount__12").value = res12;
}

function calc13() {
  let num13_1 = document.getElementById("quantity__13").value;
  let num13_2 = document.getElementById("unit__price__13").value;

  let res13 = num13_1 * num13_2;

  document.getElementById("amount__13").value = res13;
}

function calc14() {
  let num14_1 = document.getElementById("quantity__14").value;
  let num14_2 = document.getElementById("unit__price__14").value;

  let res14 = num14_1 * num14_2;

  document.getElementById("amount__14").value = res14;
}


function tax() {
  let amount1 = document.getElementById("amount__1").value;
  let amount2 = document.getElementById("amount__2").value;
  let amount3 = document.getElementById("amount__3").value;
  let amount4 = document.getElementById("amount__4").value;
  let amount5 = document.getElementById("amount__5").value;
  let amount6 = document.getElementById("amount__6").value;
  let amount7 = document.getElementById("amount__7").value;
  let amount8 = document.getElementById("amount__8").value;
  let amount9 = document.getElementById("amount__9").value;
  let amount10 = document.getElementById("amount__10").value;
  let amount11 = document.getElementById("amount__11").value;
  let amount12 = document.getElementById("amount__12").value;
  let amount13 = document.getElementById("amount__13").value;
  let amount14 = document.getElementById("amount__14").value;


  let amountTotal =
    parseInt(amount1) +
    parseInt(amount2) +
    parseInt(amount3) +
    parseInt(amount4) +
    parseInt(amount5) +
    parseInt(amount6) +
    parseInt(amount7) +
    parseInt(amount8) +
    parseInt(amount9) +
    parseInt(amount10) +
    parseInt(amount11) +
    parseInt(amount12) +
    parseInt(amount13) +
    parseInt(amount14);

  let resTax =
    Math.floor(parseInt(amountTotal) * 1.1) - parseInt(amountTotal);
  let resTotal = parseInt(amountTotal) + parseInt(resTax);
    let resSubTotal = parseInt(amountTotal)

  document.getElementById("tax").value = "";
  document.getElementById("total").value = "";
      document.getElementById("sub_total").value = "";

  document.getElementById("tax").value = resTax;
    document.getElementById("sub_total").value = resSubTotal;

  document.getElementById("total").value = resTotal;
}

function claimInfo() {
    let d1 = new Date();
    let time = d1.getTime();
        document.getElementById("claim__no").value = "";

    document.getElementById("claim__no").value = time;

    let claimDay = document.getElementById("claim__day")
    let paymentDay = document.getElementById("payment__day")

  const startDate = new Date(claim__day.value);

  // 開始日から2週間後の日付を計算
  const endDate = new Date(startDate.getTime() + 1000 * 60 * 60 * 24 * 15);
  paymentDay.value = endDate.toISOString().slice(0, 10);

}

document.getElementById("claim__no").readOnly = true;
document.getElementById("payment__day").readOnly = true;
document.getElementById("amount__1").readOnly = true;
document.getElementById("amount__2").readOnly = true;
document.getElementById("amount__3").readOnly = true;
document.getElementById("amount__4").readOnly = true;
document.getElementById("amount__5").readOnly = true;
document.getElementById("amount__6").readOnly = true;
document.getElementById("amount__7").readOnly = true;
document.getElementById("amount__8").readOnly = true;
document.getElementById("amount__9").readOnly = true;
document.getElementById("amount__10").readOnly = true;
document.getElementById("amount__11").readOnly = true;
document.getElementById("amount__12").readOnly = true;
document.getElementById("amount__13").readOnly = true;
document.getElementById("amount__14").readOnly = true;
document.getElementById("sub_total").readOnly = true;
document.getElementById("tax").readOnly = true;
document.getElementById("total").readOnly = true;


document.getElementById("claim__day").addEventListener("blur", claimInfo);

document.getElementById("quantity__1").addEventListener("blur", calc1);
document.getElementById("unit__price__1").addEventListener("blur", calc1);

document.getElementById("quantity__2").addEventListener("blur", calc2);
document.getElementById("unit__price__2").addEventListener("blur", calc2);

document.getElementById("quantity__3").addEventListener("blur", calc3);
document.getElementById("unit__price__3").addEventListener("blur", calc3);

document.getElementById("quantity__4").addEventListener("blur", calc4);
document.getElementById("unit__price__4").addEventListener("blur", calc4);

document.getElementById("quantity__5").addEventListener("blur", calc5);
document.getElementById("unit__price__5").addEventListener("blur", calc5);

document.getElementById("quantity__6").addEventListener("blur", calc6);
document.getElementById("unit__price__6").addEventListener("blur", calc6);

document.getElementById("quantity__7").addEventListener("blur", calc7);
document.getElementById("unit__price__7").addEventListener("blur", calc7);

document.getElementById("quantity__8").addEventListener("blur", calc8);
document.getElementById("unit__price__8").addEventListener("blur", calc8);

document.getElementById("quantity__9").addEventListener("blur", calc9);
document.getElementById("unit__price__9").addEventListener("blur", calc9);

document.getElementById("quantity__10").addEventListener("blur", calc10);
document.getElementById("unit__price__10").addEventListener("blur", calc10);

document.getElementById("quantity__11").addEventListener("blur", calc11);
document.getElementById("unit__price__11").addEventListener("blur", calc11);

document.getElementById("quantity__12").addEventListener("blur", calc12);
document.getElementById("unit__price__12").addEventListener("blur", calc12);

document.getElementById("quantity__13").addEventListener("blur", calc13);
document.getElementById("unit__price__13").addEventListener("blur", calc13);

document.getElementById("quantity__14").addEventListener("blur", calc14);
document.getElementById("unit__price__14").addEventListener("blur", calc14);

document.getElementById("quantity__1").addEventListener("blur", tax);
document.getElementById("unit__price__1").addEventListener("blur", tax);

document.getElementById("quantity__2").addEventListener("blur", tax);
document.getElementById("unit__price__2").addEventListener("blur", tax);

document.getElementById("quantity__3").addEventListener("blur", tax);
document.getElementById("unit__price__3").addEventListener("blur", tax);

document.getElementById("quantity__4").addEventListener("blur", tax);
document.getElementById("unit__price__4").addEventListener("blur", tax);

document.getElementById("quantity__5").addEventListener("blur", tax);
document.getElementById("unit__price__5").addEventListener("blur", tax);

document.getElementById("quantity__6").addEventListener("blur", tax);
document.getElementById("unit__price__6").addEventListener("blur", tax);

document.getElementById("quantity__7").addEventListener("blur", tax);
document.getElementById("unit__price__7").addEventListener("blur", tax);

document.getElementById("quantity__8").addEventListener("blur", tax);
document.getElementById("unit__price__8").addEventListener("blur", tax);

document.getElementById("quantity__9").addEventListener("blur", tax);
document.getElementById("unit__price__9").addEventListener("blur", tax);

document.getElementById("quantity__10").addEventListener("blur", tax);
document.getElementById("unit__price__10").addEventListener("blur", tax);

document.getElementById("quantity__11").addEventListener("blur", tax);
document.getElementById("unit__price__11").addEventListener("blur", tax);

document.getElementById("quantity__12").addEventListener("blur", tax);
document.getElementById("unit__price__12").addEventListener("blur", tax);

document.getElementById("quantity__13").addEventListener("blur", tax);
document.getElementById("unit__price__13").addEventListener("blur", tax);

document.getElementById("quantity__14").addEventListener("blur", tax);
document.getElementById("unit__price__14").addEventListener("blur", tax);

let clearBtn = document.getElementById("clear__btn");
