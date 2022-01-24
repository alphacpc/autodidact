import 'dart:ffi';

void main(){
  print("*****LES SEQUENCES******");

  List listMixed = ["Alpha", 25, false, 1.69];
  List<String> family = ["Mouhamed", "Awa", "Alpha"];
  List<int> favoriteNumber = [04, 14, 24, 34, 44, 54];
  List<bool> checked = [true, false];
  List<double> float = [3.14, 9.1, 23];


  print("***Liste mix*****");
  showElements(listMixed);
  showElementByIndex(listMixed, 2);

  print("***Liste Family*****");
  showElements(family);
  showElementByIndex(family, 3);


  print("***Liste Favorite Number*****");
  showElements(favoriteNumber);
  showElementByIndex(favoriteNumber, 1);


  print("***Liste Checked*****");
  showElements(checked);
  showElementByIndex(checked, 1);


  print("***Liste Floating*****");
  showElements(float);
  showElementByIndex(float, 0);


  
}

void showElements(myList){
  myList.forEach((el) => print(el));
}

void showElementByIndex(myList, position){

  if(position >= myList.length){
    print("La premiere valeur est de : " + myList[0]);
  }


  print(myList.length);
  print(myList[position]);

}