var generate = function(numRows) {
    let ans = [[1]]
    if(numRows > 1) {
        for(let i = 1; i < numRows; i++) {
            if(i == 1) {
                ans.push([ans[0][0],1])
            } else {
                let temp = []
                for(let n = 0; n < ans[i - 1].length - 1; n++) {
                    let mid = ans[i - 1][n] + ans[i - 1][n+1]
                    temp.push(mid)
                }
                temp = [1,...temp,1]
                ans.push(temp)
            }
        }
    }
    return ans
};

console.log(generate(6))