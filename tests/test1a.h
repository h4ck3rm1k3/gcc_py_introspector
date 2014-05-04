class Foo {};
template<typename _Tp, typename _Alloc = Foo >
  class deque  {  };
  template<typename _Tp, typename _Alloc> void bar(const deque<_Tp, _Alloc>& __x);
