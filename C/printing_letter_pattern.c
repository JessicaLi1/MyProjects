/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush04.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: dli <dl@student.42wolfsburg.de>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2022/09/18 18:41:35 by dli               #+#    #+#             */
/*   Updated: 2022/09/18 18:41:35 by dli              ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}

void	ft_print_column_1(int co)
{
	ft_putchar('A');
	ft_putchar('\n');
	co = co - 2;
	while (--co >= 0)
	{
		ft_putchar('B');
		ft_putchar('\n');
	}	
	ft_putchar('C');
	ft_putchar('\n');
}

void	ft_print_row_1(int r)
{
	r = r - 2;
	ft_putchar('A');
	while (--r >= 0)
	{
		ft_putchar('B');
	}	
	ft_putchar('C');
	ft_putchar('\n');
}

void	ft_print_row_reverse(int w)
{
	w = w - 2;
	ft_putchar('C');
	while (--w >= 0)
	{
		ft_putchar('B');
	}		
	ft_putchar('A');
	ft_putchar('\n');
}

void	ft_print_body(int b, int d)
{
	int	k;

	d = d - 2;
	while (--d >= 0)
	{
		ft_putchar('B');
		k = b - 2;
		while (--k >= 0)
		{
			ft_putchar(' ');
		}
		ft_putchar('B');
		ft_putchar('\n');
	}		
}

void	ft_printing_main(int x, int y)
{
	if (x == 1 && y == 1)
	{
		ft_putchar('A');
		ft_putchar('\n');
		return ;
	}
	else
	{
		if (x == 1)
		{
			ft_print_column_1(y);
			return ;
		}
		if (y == 1)
		{
			ft_print_row_1(x);
			return ;
		}
		else
		{
			ft_print_row_1(x);
			ft_print_body(x,y);
			ft_print_row_reverse(x);
			return ;
		}
	}
}

int	main(void)
{
	int	i;
	int	j;

	i = 5;
	j = 3;
	ft_printing_main(i, j);
	return (0);
}
