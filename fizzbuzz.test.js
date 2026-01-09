// FizzBuzz 関数化
function fizzbuzz(n) {
  let out = '';
  if(n%3===0) out+='Fizz';
  if(n%5===0) out+='Buzz';
  return out||n;
}

describe('FizzBuzz', () => {
  
  describe('15の倍数（FizzBuzz）', () => {
    test('15は"FizzBuzz"を返す', () => {
      expect(fizzbuzz(15)).toBe('FizzBuzz');
    });
  });

  describe('3の倍数（Fizz）', () => {
    test('3は"Fizz"を返す', () => {
      expect(fizzbuzz(3)).toBe('Fizz');
    });
    test('6は"Fizz"を返す', () => {
      expect(fizzbuzz(6)).toBe('Fizz');
    });
    test('9は"Fizz"を返す', () => {
      expect(fizzbuzz(9)).toBe('Fizz');
    });
    test('12は"Fizz"を返す', () => {
      expect(fizzbuzz(12)).toBe('Fizz');
    });
    test('18は"Fizz"を返す', () => {
      expect(fizzbuzz(18)).toBe('Fizz');
    });
  });

  describe('5の倍数（Buzz）', () => {
    test('5は"Buzz"を返す', () => {
      expect(fizzbuzz(5)).toBe('Buzz');
    });
    test('10は"Buzz"を返す', () => {
      expect(fizzbuzz(10)).toBe('Buzz');
    });
    test('20は"Buzz"を返す', () => {
      expect(fizzbuzz(20)).toBe('Buzz');
    });
  });

  describe('その他の数値', () => {
    test('1は1を返す', () => {
      expect(fizzbuzz(1)).toBe(1);
    });
    test('2は2を返す', () => {
      expect(fizzbuzz(2)).toBe(2);
    });
    test('4は4を返す', () => {
      expect(fizzbuzz(4)).toBe(4);
    });
    test('7は7を返す', () => {
      expect(fizzbuzz(7)).toBe(7);
    });
    test('8は8を返す', () => {
      expect(fizzbuzz(8)).toBe(8);
    });
    test('11は11を返す', () => {
      expect(fizzbuzz(11)).toBe(11);
    });
    test('13は13を返す', () => {
      expect(fizzbuzz(13)).toBe(13);
    });
    test('14は14を返す', () => {
      expect(fizzbuzz(14)).toBe(14);
    });
    test('16は16を返す', () => {
      expect(fizzbuzz(16)).toBe(16);
    });
    test('17は17を返す', () => {
      expect(fizzbuzz(17)).toBe(17);
    });
    test('19は19を返す', () => {
      expect(fizzbuzz(19)).toBe(19);
    });
  });

  describe('失敗例', () => {
    test('3は"Buzz"を返す（意図的な失敗）', () => {
      expect(fizzbuzz(3)).toBe('Buzz'); // これは失敗する
    });
  });

});
