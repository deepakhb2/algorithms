def insertion_sort(arr)
  for i in (1...arr.length) do
    key = arr[i]
    j = i-1
    while(j >= 0 && key < arr[j])
      arr[j+1] = arr[j]
      j -= 1
    end
    arr[j+1] = key
  end
end

numbers = [23,43,21,2,3,56,99,283]
insertion_sort(numbers)
puts(numbers)
