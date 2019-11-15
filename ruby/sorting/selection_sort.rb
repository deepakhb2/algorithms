def selection_sort(arr)
  length = arr.length
  for i in (0...length) do
    min_i = i
    for j in (i+1...length) do
      if(arr[min_i] > arr[j])
        min_i = j
      end
    end
    arr[i], arr[min_i] = arr[min_i], arr[i]
  end
end

numbers = [23,43,21,2,3,56,99,80]
selection_sort(numbers)
puts(numbers)
