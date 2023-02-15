function solution(n) {
  const arr = Array(n + 1).fill(0)
  for (let i = 0; i <= n; i++) {
    arr[i] = i
    for (let j = 1; j * j <= i; j++) {
      arr[i] = Math.min(arr[i], 1 + arr[i - j * j])
    }
  }
  return arr[n]
}