
namespace std
{
  typedef long unsigned int size_t;
  typedef long int ptrdiff_t;
}

namespace std __attribute__ ((__visibility__ ("default")))
{
  template<typename _Tp>
    inline _Tp*
    __addressof(_Tp& __r)
    {
      return reinterpret_cast<_Tp*>
 (&const_cast<char&>(reinterpret_cast<const volatile char&>(__r)));
    }
}


namespace std __attribute__ ((__visibility__ ("default")))
{
  void
  __throw_bad_alloc(void) __attribute__((__noreturn__));
};

namespace __gnu_cxx __attribute__ ((__visibility__ ("default")))
{
  using std::size_t;
  using std::ptrdiff_t;
  template<typename _Tp>
    class new_allocator
    {
    public:
      typedef size_t size_type;
      typedef ptrdiff_t difference_type;
      typedef _Tp* pointer;
      typedef const _Tp* const_pointer;
      typedef _Tp& reference;
      typedef const _Tp& const_reference;
      typedef _Tp value_type;
      template<typename _Tp1>
        struct rebind
        { typedef new_allocator<_Tp1> other; };
      new_allocator() throw() { }
      new_allocator(const new_allocator&) throw() { }
      template<typename _Tp1>        new_allocator(const new_allocator<_Tp1>&) throw() { }
      ~new_allocator() throw() { }
      pointer address(reference __x) const      { return std::__addressof(__x); }
      const_pointer  address(const_reference __x) const       { return std::__addressof(__x); }
      pointer allocate(size_type __n, const void* = 0)      {
        if (__n > this->max_size())
          std::__throw_bad_alloc();        
        return static_cast<_Tp*>(::operator new(__n * sizeof(_Tp)));
      }

      void       deallocate(pointer __p, size_type)      { 
        ::operator delete(__p); 
      }

      size_type     max_size() const throw()
      { return size_t(-1) / sizeof(_Tp); }

      void
      construct(pointer __p, const _Tp& __val)
      { ::new((void *)__p) _Tp(__val); }

      void
      destroy(pointer __p) { __p->~_Tp(); }

    };

  template<typename _Tp>
    inline bool
    operator==(const new_allocator<_Tp>&, const new_allocator<_Tp>&)
    { return true; }

  template<typename _Tp>
    inline bool
    operator!=(const new_allocator<_Tp>&, const new_allocator<_Tp>&)
    { return false; }
}

namespace std __attribute__ ((__visibility__ ("default")))
{

  template<typename _Tp>
    class allocator: public __gnu_cxx::new_allocator<_Tp>
    {
   public:
      typedef size_t size_type;
      typedef ptrdiff_t difference_type;
      typedef _Tp* pointer;
      typedef const _Tp* const_pointer;
      typedef _Tp& reference;
      typedef const _Tp& const_reference;
      typedef _Tp value_type;

      template<typename _Tp1>
        struct rebind
        { typedef allocator<_Tp1> other; };

      allocator() throw() { }
      allocator(const allocator& __a) throw()      : __gnu_cxx::new_allocator<_Tp>(__a) { }
      template<typename _Tp1>        allocator(const allocator<_Tp1>&) throw() { }
      ~allocator() throw() { }

    };
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
