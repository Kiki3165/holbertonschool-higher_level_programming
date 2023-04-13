#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const n = args.length;

if (n === 0) {
  console.log(0);
} else if (n === 1) {
  console.log(0);
} else {
  let max1 = args[0];
  let max2 = args[1];
  if (max2 > max1) {
    [max1, max2] = [max2, max1];
  }
  for (let i = 2; i < n; i++) {
    if (args[i] > max1) {
      max2 = max1;
      max1 = args[i];
    } else if (args[i] > max2) {
      max2 = args[i];
    }
  }
  console.log(max2);
}
