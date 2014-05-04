
namespace __gnu_cxx 
{
  template<typename _Tp>
    class new_allocator
    {
    };
}

namespace std 
{

  template<typename _Tp>
    class allocator: public __gnu_cxx::new_allocator<_Tp>    { };
}

  template<typename _Tp, typename _Alloc>
    class _Deque_base
    {
    public:
    };

template<typename _Tp, typename _Alloc = std::allocator<_Tp> >
  class deque : protected _Deque_base<_Tp, _Alloc>
  {
  };

  /// Based on operator==
  template<typename _Tp, typename _Alloc>
    inline bool
    operator!=(const deque<_Tp, _Alloc>& __x,
	       const deque<_Tp, _Alloc>& __y)
    { return !(__x == __y); }
